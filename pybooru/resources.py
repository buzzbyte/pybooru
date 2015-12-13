# -*- coding: utf-8 -*-

"""This module contains all resources for pybooru.

site_list:
    Is a dict that contains various based Danbooru/Moebooru, default sites.
api_base_url:
    Is a dict that contains the urls for API functions.
http_status_codes:
    Is a dict that contains the http status code for Danbooru/Moebooru API.
"""


# Default SITE_LIST
SITE_LIST = {
    'konachan': {
        'url': "http://konachan.com",
        'hashed_string': "So-I-Heard-You-Like-Mupkids-?--{0}--"},

    'yandere': {
        'url': "https://yande.re",
        'hashed_string': "choujin-steiner--{0}--"}
    }


# API_BASE_URL for the API functions
API_BASE_URL_MOE = {
    'posts_list': {
        'url': "/post.json",
        'method':"POST",
        'required_login': False},
    'posts_create': {
        'url': "/post/create.json",
        'method':"POST",
        'required_login': True},
    'posts_update': {
        'url': "/post/update.json",
        'method':"POST",
        'required_login': True},
    'posts_destroy': {
        'url': "/post/destroy.json",
        'method':"POST",
        'required_login': True},
    'posts_revert_tags': {
        'url': "/post/revert_tags.json",
        'method':"POST",
        'required_login': True},
    'posts_vote': {
        'url': "/post/vote.json",
        'method':"POST",
        'required_login': True},
    'tags_list': {
        'url': "/tag.json",
        'method':"POST",
        'required_login': False},
    'tags_update': {
        'url': "/tag/update.json",
        'method':"POST",
        'required_login': True},
    'tags_related': {
        'url': "/tag/related.json",
        'method':"POST",
        'required_login': False},
    'artists_list': {
        'url': "/artist.json",
        'method':"POST",
        'required_login': False},
    'artists_create': {
        'url': "/artist/create.json",
        'method':"POST",
        'required_login': True},
    'artists_update': {
        'url': "/artist/update.json",
        'method':"POST",
        'required_login': True},
    'artists_destroy': {
        'url': "/artist/destroy.json",
        'method':"POST",
        'required_login': True},
    'comments_show': {
        'url': "/comment/show.json",
        'method':"POST",
        'required_login': False},
    'comments_create': {
        'url': "/comment/create.json",
        'method':"POST",
        'required_login': True},
    'comments_destroy': {
        'url': "/comment/destroy.json",
        'method':"POST",
        'required_login': True},
    'wiki_list': {
        'url': "/wiki.json",
        'method':"POST",
        'required_login': False},
    'wiki_create': {
        'url': "/wiki/create.json",
        'method':"POST",
        'required_login': True},
    'wiki_update': {
        'url': "/wiki/update.json",
        'method':"POST",
        'required_login': True},
    'wiki_show': {
        'url': "/wiki/show.json",
        'method':"POST",
        'required_login': False},
    'wiki_destroy': {
        'url': "/wiki/destroy.json",
        'method':"POST",
        'required_login': True},
    'wiki_lock': {
        'url': "/wiki/lock.json",
        'method':"POST",
        'required_login': True},
    'wiki_unlock': {
        'url': "/wiki/unlock.json",
        'method':"POST",
        'required_login': True},
    'wiki_revert': {
        'url': "/wiki/revert.json",
        'method':"POST",
        'required_login': True},
    'wiki_history': {
        'url': "/wiki/history.json",
        'method':"POST",
        'required_login': False},
    'notes_list': {
        'url': "/note.json",
        'method':"POST",
        'required_login': False},
    'notes_search': {
        'url': "/note/search.json",
        'method':"POST",
        'required_login': False},
    'notes_history': {
        'url': "/note/history.json",
        'method':"POST",
        'required_login': False},
    'notes_revert': {
        'url': "/note/revert.json",
        'method':"POST",
        'required_login': True},
    'notes_create_update': {
        'url': "/note/update.json",
        'method':"POST",
        'required_login': True},
    'users_search': {
        'url': "/user.json",
        'method':"POST",
        'required_login': False},
    'forum_list': {
        'url': "/forum.json",
        'method':"POST",
        'required_login': False},
    'pools_list': {
        'url': "/pool.json",
        'method':"POST",
        'required_login': False},
    'pools_posts': {
        'url': "/pool/show.json",
        'method':"POST",
        'required_login': False},
    'pools_update': {
        'url': "/pool/update.json",
        'method':"POST",
        'required_login': True},
    'pools_create': {
        'url': "/pool/create.json",
        'method':"POST",
        'required_login': True},
    'pools_destroy': {
        'url': "/pool/destroy.json",
        'method':"POST",
        'required_login': True},
    'pools_add_post': {
        'url': "/pool/add_post.json",
        'method':"POST",
        'required_login': True},
    'pools_remove_post': {
        'url': "/pool/remove_post.json",
        'method':"POST",
        'required_login': True},
    'favorites_list_users': {
        'url': "/favorite/list_users.json",
        'method':"POST",
        'required_login': False}
    }

API_BASE_URL_1 = {
    # TODO finish this.
}

API_BASE_URL_2 = {
    'posts_list': {
        'url': "/posts.json",
        'method':"GET",
        'required_login': False},
    'posts_create': {
        'url': "/uploads.json",
        'method':"POST",
        'required_login': True},
    'posts_update': {
        'url': "/posts/update.json",
        'method':"PUT",
        'required_login': True},
    'posts_destroy': {
        'url': "/posts/destroy.json",
        'method':"POST",
        'required_login': True},
    'posts_revert_tags': {
        'url': "/posts/revert.json",
        'method':"PUT",
        'required_login': True},
    'posts_vote': {
        'url': "/posts/votes.json",
        'method':"POST",
        'required_login': True},
    'tags_list': {
        'url': "/tags.json",
        'method':"GET",
        'required_login': False},
    'tags_update': {
        'url': "/tags/update.json",
        'method':"POST",
        'required_login': True},
    'tags_related': {
        'url': "/related_tag.json",
        'method':"GET",
        'required_login': False},
    'artists_list': {
        'url': "/artists.json",
        'method':"GET",
        'required_login': False},
    'artists_create': {
        'url': "/artists.json",
        'method':"POST",
        'required_login': True},
    'artists_update': {
        'url': "/artists/update.json",
        'method':"PUT",
        'required_login': True},
    'artists_destroy': {
        'url': "/artists/destroy.json",
        'method':"POST",
        'required_login': True},
    'comments_show': {
        'url': "/comments/show.json",
        'method':"GET",
        'required_login': False},
    'comments_create': {
        'url': "/comments.json",
        'method':"POST",
        'required_login': True},
    'comments_destroy': {
        'url': "/comments/destroy.json",
        'method':"POST",
        'required_login': True},
    'wiki_list': {
        'url': "/wiki_pages.json",
        'method':"GET",
        'required_login': False},
    'wiki_create': {
        'url': "/wiki_pages.json",
        'method':"POST",
        'required_login': True},
    'wiki_update': {
        'url': "/wiki_pages/update.json",
        'method':"PUT",
        'required_login': True},
    'wiki_show': {
        'url': "/wiki_pages/show.json",
        'method':"GET",
        'required_login': False},
    'wiki_destroy': {
        'url': "/wiki_pages/destroy.json",
        'method':"POST",
        'required_login': True},
    'wiki_lock': {
        'url': "/wiki_pages/lock.json",
        'method':"POST",
        'required_login': True},
    'wiki_unlock': {
        'url': "/wiki_pages/unlock.json",
        'method':"POST",
        'required_login': True},
    'wiki_revert': {
        'url': "/wiki_pages/revert.json",
        'method':"PUT",
        'required_login': True},
    'wiki_history': {
        'url': "/wiki_pages/history.json",
        'method':"GET",
        'required_login': False},
    'notes_list': {
        'url': "/notes.json",
        'method':"GET",
        'required_login': False},
    'notes_revert': {
        'url': "/notes/revert.json",
        'method':"PUT",
        'required_login': True},
    'notes_create_update': {
        'url': "/notes/update.json",
        'method':"PUT",
        'required_login': True},
    'users_search': {
        'url': "/users.json",
        'method':"GET",
        'required_login': False},
    'forum_list': {
        'url': "/forum_topics.json",
        'method':"GET",
        'required_login': False},
    'pools_list': {
        'url': "/pools.json",
        'method':"GET",
        'required_login': False},
    'pools_posts': {
        'url': "/pools/show.json",
        'method':"GET",
        'required_login': False},
    'pools_update': {
        'url': "/pools/update.json",
        'method':"PUT",
        'required_login': True},
    'pools_create': {
        'url': "/pools.json",
        'method':"POST",
        'required_login': True},
    'pools_destroy': {
        'url': "/pools/destroy.json",
        'method':"POST",
        'required_login': True},
    'favorites_list_users': {
        'url': "/favorites/list_users.json",
        'method':"GET",
        'required_login': False}
    }

# HTTP_STATUS_CODES
HTTP_STATUS_CODES = {
    200: ("OK", "Request was successful"),
    403: ("Forbidden", "Access denied"),
    404: ("Not Found", "Not found"),
    420: ("Invalid Record", "Record could not be saved"),
    421: ("User Throttled", "User is throttled, try again later"),
    422: ("Locked", "The resource is locked and cannot be modified"),
    423: ("Already Exists", "Resource already exists"),
    424: ("Invalid Parameters", "The given parameters were invalid"),
    500: ("Internal Server Error", "Some unknown error occurred on the server"),
    503: ("Service Unavailable", "Server cannot currently handle the request")
    }
