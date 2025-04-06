Tags
====

This module allows you to create, view, and delete tags.


HTTP Endpoints
''''''''''''''

.. http:get:: /tags/

  Allows you to view all tags.


.. http:post:: /tags/<tag>

  Allows you to add a new tag.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``tag``
      - ``str``
      - Yes
      - The name of the tag you'd like to add.

  .. warning::
    This endpoint requires authentification token provided in the ``Authorization`` header.


  .. admonition:: Status Codes

    This endpoint can return ``401`` status code.  

.. http:delete:: /tags/<tag>

  Allows you to remove a tag.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``tag``
      - ``str``
      - Yes
      - The name of the tag you'd like to add.

  .. warning::
    This endpoint requires authentification token provided in the ``Authorization`` header.

  .. attention::

    This endpoint requires admin status.

  .. admonition:: Status Codes

    This endpoint can return ``401`` or ``404`` status code.


**Example request**:

   .. sourcecode:: http

      GET /users/123/posts/web HTTP/1.1
      Host: example.com
      Accept: application/json, text/javascript

**Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      [
        {
          "post_id": 12345,
          "author_id": 123,
          "tags": ["server", "web"],
          "subject": "I tried Nginx"
        },
        {
          "post_id": 12346,
          "author_id": 123,
          "tags": ["html5", "standards", "web"],
          "subject": "We go to HTML 5"
        }
      ]