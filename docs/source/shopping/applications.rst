Applications
============

This module allows you to view application data and modify :ref:`application's state<Application State>`.
It also allows you to create, view, search for, modify, and delete tags and products assigned to an application.

.. note::
  All endpoints in this module will create a new application if one does not already exist (except ``GET /application/``).
  If you create your account using the :ref:`user module <User Module>`, your application have been automatically created as well.

.. warning::
  All endpoints in this module require authentification token provided in the ``Authorization`` header.

Application State
'''''''''''''''''''''

Each user is assigned the following application state:

.. list-table::
  :widths: 25 10 10 30
  :header-rows: 1

  * - State
    - Type
    - Required
    - Description
  * - ``back``
    - ``Boolean``
    - Yes
    -  Whether the page should go back
  * - ``dialogflowUpdated``
    - ``Boolean``
    - Yes
    - Whether the last update was from dialogflow (only used by GUI)
  * - ``page``
    - ``str``
    - Yes
    - The URI of that the page should go to (minus the host)

  


HTTP Endpoints
''''''''''''''

.. http:get:: /application/

  Allows you to view your application data.


.. http:get:: /application/tags/

  Allows you to view all tags assigned to your application.

.. http:get:: /application/products/

  Allows you to view all products and their amounts that have been added to your shopping cart.


.. http:get:: /application/products/<product_id>

  Allows you to view a product that has been added to your shopping cart.
  If successful, this endpoint returns product's information.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``product_id``
      - ``int``
      - Yes
      - The id of a product.

  .. admonition:: Status Codes

    If the product hasn't been found, ``404`` status code is returned. 

.. http:post:: /application/tags/<tag>

  Allows you to add a new tag to your application. 

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - tag
      - ``str``
      - Yes
      - The name of the tag.

  .. admonition:: Status Codes

    This endpoint will return ``404`` status code to confirm that you're not duplicating tags.


.. http:post:: /application/products/<product_id>

  Allows you to add a new product to your application cart. 

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``product_id``
      - ``int``
      - Yes
      - The id of a product.

  .. admonition:: Status Codes

    This endpoint will return ``404`` status code to confirm that you're not duplicating products.
  

.. http:delete:: /application/tags/

  Allows you to remove all tags from your application.

.. http:delete:: /application/tags/<tag>

  Allows you to remove a single tag from your application.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - tag
      - ``str``
      - Yes
      - The name of the tag.

  .. admonition:: Status Codes

    If the tag hasn't been found, ``404`` status code is returned.


.. http:delete:: /application/products/

  Allows you to remove all products from your application's cart.


.. http:delete:: /application/products/<product_id>

  Allows you to remove a single products from your application's cart.
  
  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``product_id``
      - ``int``
      - Yes
      - The id of a product.

  .. admonition:: Status Codes

    If the product hasn't been found, ``404`` status code is returned.


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