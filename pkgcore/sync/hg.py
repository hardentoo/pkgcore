# Copyright: 2006 Brian Harring <ferringb@gmail.com>
# License: GPL2

from pkgcore.sync import base

class hg_syncer(base.dvcs_syncer):

    binary = "hg"

    supported_uris = (
        ('hg+', 5),
        ('mercurial+', 5),
        )

    @staticmethod
    def parse_uri(raw_uri):
        if raw_uri.startswith("hg+"):
            return raw_uri[3:]
        elif raw_uri.startswith("mercurial+"):
            return raw_uri[len("mercurial+"):]
        raise base.uri_exception(raw_uri, "doesn't start with hg+"
            " nor mercurial+")

    def __init__(self, basedir, uri, **kwargs):
        uri = self.parse_uri(uri)
        base.dvcs_syncer.__init__(self, basedir, uri, **kwargs)

    def _initial_pull(self):
        return [self.binary_path, "clone", self.uri, self.basedir]

    def _update_existing(self):
        return [self.binary_path, "pull", "-u", self.uri]
