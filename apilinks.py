#!/usr/bin/env python
# -*- coding: utf-8-sig -*-

def make_api_link(name, rawtext, text, lineno, inliner,
                     options={}, content=[]):

    from docutils import nodes, utils

    # quick, dirty, and ugly...
    if '<' in text and '>' in text:
        full_name, label = text.split('<')
        full_name = full_name.strip()
        label = label.strip('>').strip()
    else:
        full_name = text
        label = full_name

    #get the base url for api links from the config file
    env = inliner.document.settings.env
    base_url =  env.config.apilinks_base_url

    # not really sufficient, but just testing...
    # ...hmmm, maybe this is good enough after all
    ref = ''.join((base_url, full_name, '.html'))

    node = nodes.reference(rawtext, utils.unescape(label), refuri=ref,
                           **options)

    nodes = [node]
    sys_msgs = []
    return nodes, sys_msgs


# setup function to register the extension

def setup(app):
    app.add_config_value('apilinks_base_url', 
                         'https://twistedmatrix.com/documents/current/api/', 
                         'env')
    app.add_role('api', make_api_link)
