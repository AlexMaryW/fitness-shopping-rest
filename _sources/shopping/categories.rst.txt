Categories
==========

This module allows you to create, view, and delete categories. 
It also allows you to view tags assigned to a category.


HTTP Endpoints
''''''''''''''

.. http:get:: /categories/

  Allows you to view all categories.


.. http:get:: /categories/<category>/tags/

  Allows you to view all tags assigned to a category.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``category``
      - ``str``
      - Yes
      - The name of the category whose tags you'd like to view.
  
  .. admonition:: Status Codes

    If the category hasn't been found, ``404`` status code is returned.

.. http:post:: /categories/<category>

  Allows you to add a new category. 

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``category``
      - ``str``
      - Yes
      - The name of the category you'd like to add.


  .. warning::
    This endpoint requires authentification token provided in the ``Authorization`` header.

  .. attention::

    This endpoint requires admin status.


  .. admonition:: Status Codes

    This endpoint can return ``401`` status code.
   

.. http:delete:: /categories/<category>

  Allows you to remove a category.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``category``
      - ``str``
      - Yes
      - The name of the category you'd like to remove.


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