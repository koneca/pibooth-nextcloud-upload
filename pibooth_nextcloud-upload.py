# -*- coding: utf-8 -*-

"""Pibooth plugin to upload pictures to your nextcloud."""

import json
import os.path

import requests
import owncloud

import pibooth
from pibooth.utils import LOGGER


__version__ = "1.0.0"


@pibooth.hookimpl
def pibooth_configure(cfg):
    """Declare the new configuration options"""
    cfg.add_option('NEXTCLOUD', 'directory_name', "Pibooth",
                   "Directory where pictures are uploaded",
                   "Directory name", "Pibooth")
    cfg.add_option('NEXTCLOUD', 'client_credentials', '',
                   "Credentials for the nextcloud instance")
    cfg.add_option('NEXTCLOUD', 'server_name', '',
                   "Url to the nextcloud instance")

@pibooth.hookimpl
def pibooth_startup(app, cfg):
    """Create the NextcloudUpload instance."""
    app.Nextcloud_upload = NextcloudApi(cfg.getpath('NEXTCLOUD', 'client_credentials'), cfg.getpath('NEXTCLOUD', 'server_name'), cfg.getpath('NEXTCLOUD', 'directory_name'))


@pibooth.hookimpl
def state_processing_exit(app, cfg):
    """Upload picture to nextcloud directory"""
    picture = (app.previous_picture_file)
    app.Nextcloud_upload.upload(picture, cfg.get('NEXTCLOUD', 'directory_name'))
    link = app.Nextcloud_upload.get_file_link(picture, cfg.get('NEXTCLOUD', 'directory_name'))
    app.add_option('NEXTCLOUD', 'current_link', link)


class NextcloudApi(object):

    """Class handling connections to nextcloud.

    A file with YOUR_CLIENT_ID and YOUR_CLIENT_SECRET is required, go to
    https://developers.google.com/photos/library/guides/get-started .


    :param client_id: file generated from google API
    :type client_id: str
    :param credentials_filename: name of the file to store authorization
    :type credentials_filename: str
    """

    URL = 'https://photoslibrary.googleapis.com/v1'
    SCOPES = ['https://www.googleapis.com/auth/photoslibrary',
              'https://www.googleapis.com/auth/photoslibrary.sharing']

    def __init__(self, client_credentials, server_name,directory_name):
        self.client_credentials = client_credentials

        self.activated = True
        self.server_name = server_name
        self.directory_name = directory_name

        self._credentials = None
        if not self.is_reachable():
            self._session = None
        else:
            oc = owncloud.Client('http://domain.tld/owncloud')
            self.oc = oc
            oc.login(self.client_credentials[0], self.client_credentials[1])
            
            self.create_dir()
            

    def is_reachable(self):
        """Check if Nextcloud instance is reachable."""
        try:
            return requests.get(self.server_name).status_code == 200
        except requests.ConnectionError:
            return False

    def create_dir(self):
        entries = self.oc.list('/')
        found = False
        for entry in entries:
            if self.directory_name == entry:
                found = True
                continue
        
        if not found:
            self.oc.mkdir(self.directory_name)
            
            
    def upload(self, photo_files, directory_name):
        """Upload a picture files to the given nextcloud dir."""

        if not directory_name.endswith('/'):
            directory_name += '/'
            
        self.oc.put_file(directory_name, photo_files)
        
    def get_file_link(self, photo_file, directory_name):
        if not directory_name.endswith('/'):
            directory_name += '/'
        
        return link_info = self.oc.share_file_with_link(directory_name + photo_file)