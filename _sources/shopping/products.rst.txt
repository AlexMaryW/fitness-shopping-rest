Products
========

This module allows you to create, view, search for, modify, and delete products. 
It also allows you to create and delete tags assigned to a product.

Product Information
'''''''''''''''''''

Each product can be assigned the following information:

.. list-table::
  :widths: 25 10 10 30
  :header-rows: 1

  * - Attribute
    - Type
    - Required
    - Description
  * - Name
    - ``str``
    - No
    - The product's name, e.g. "jeans".
  * - Category
    - ``str``
    - No
    - The product's category e.g. "trousers".
  * - Count
    - ``int``
    - No
    - The amount of product in your cart.
  * - Description
    - ``str``
    - No
    - Description of the product, e.g. "Straight black jeans"
  * - Image
    - ``str``
    - No
    - URL to an image of the product.
  * - Price
    - ``float``
    - No
    - The product's price, e.g. $25.99.
  
.. note::
  The default value of each attribute is ``None``.

HTTP Endpoints
''''''''''''''

.. http:get:: /products/

  Allows you to view all products and :ref:`their information<Product Information>`.


.. http:get:: /products/<product_id>

  Allows you to search for a product.
  If successful, the endpoint returns :ref:`product's information<Product Information>`.

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
      - The id of a product which you'd like to view.


  .. admonition:: Status Codes

    If a product hasn't been found, ``404`` status code is returned.

.. http:get:: /products/<product_id>/tags/

  Allows you to view tags assigned to a product.

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
      - The id of a product whose tags you'd like to view.


  .. admonition:: Status Codes

    If a product hasn't been found, ``404`` status code is returned.

.. http:post:: /products/

  Allows you to add a new product. 
  For each unique product, you can add :ref:`its information<Product Information>` as well as tags and review.

  .. warning:: 

    This endpoint requires authentification token provided in the ``Authorization`` header.

  .. attention::

    This endpoint requires admin status.

  .. admonition:: Status Codes

    This endpoint can return ``403`` or ``400`` status code.

.. http:post:: /products/<product_id>/tag/<tag>

  Allows you to add a new tag to a product.

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
      - The id of a product to which you'd like to assign a tag.
    * - ``tag``
      - ``str``
      - Yes
      - The name of the tag you'd like to add to the product.

  .. warning:: 

    This endpoint requires authentification token provided in the ``Authorization`` header.

  .. attention::

    This endpoint requires admin status.

  .. admonition:: Status Codes

    This endpoint can return ``403`` or ``404`` status code.


.. http:put:: /products/<product_id>

  Allows you to modify :ref:`product's information<Product Information>`.

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
      - The id of a product you'd like to modify.

  .. warning:: 

    This endpoint requires authentification token provided in the ``Authorization`` header.

  .. attention::

    This endpoint requires admin status.

  .. admonition:: Status Codes

    This endpoint can return ``403``, ``404``, or ``400`` status code.
  

.. http:delete:: /products/<product_id>/

  Allows you to remove a product.

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
      - The id of a product you'd like to delete.

  .. warning:: 

    This endpoint requires authentification token provided in the ``Authorization`` header.

  .. attention::

    This endpoint requires admin status.

  .. admonition:: Status Codes
    
    This endpoint can return ``404`` or ``403`` status code.


.. http:delete:: /products/<product_id>/tags/<tag>

  Allows you to remove a tag assigned to a product.

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
      - The id of a product to which the tag you want to delete is assigned.
    * - ``tag``
      - ``str``
      - Yes
      - The tag you'd like to delete.

  .. warning:: 

    This endpoint requires authentification token provided in the ``Authorization`` header.

  .. attention::

    This endpoint requires admin status.

  .. admonition:: Status Codes
    
    This endpoint can return ``404`` or ``403`` status code.


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