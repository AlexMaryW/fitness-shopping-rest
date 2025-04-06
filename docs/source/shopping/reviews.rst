Reviews
=======

This module allows you to create, view, search for, modify, and delete product reviews.


Review Information
''''''''''''''''''

Each review can be assigned the following information:

.. list-table::
  :widths: 25 10 10 30
  :header-rows: 1

  * - Attribute
    - Type
    - Required
    - Description
  * - ``product_id``
    - ``int``
    - Yes
    - The id of the reviewed product.
  * - Title
    - ``str``
    - No
    - The title of your review, e.g. "Perfect Jogging Shoes"
  * - Stars
    - ``float``
    - No
    - The amount of stars you want to award the product, e.g. 4.5.
  * - Text
    - ``str``
    - No
    - The content of your review. You can make it as long as you wish.

  
.. note::
  The default value of all attributes, except ``product_id``, is ``None``.

HTTP Endpoints
''''''''''''''

.. http:get:: /products/<product_id>/reviews/

  Allows you to view all reviews assigned to a product.

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
      - The id of a product whose reviews you'd like to view.

  .. admonition:: Status Codes

    If the product hasn't been found, ``404`` status code is returned.

.. http:get:: /products/<product_id>/reviews/<review_id>

  Allows you to search for review of a product.
  If successful, the endpoint returns :ref:`the review's information<Review Information>`.

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
      - The id of a product whose review you'd like to view.
    * - ``review_id``
      - ``int``
      - Yes
      - The id the review you're looking for.

  .. admonition:: Status Codes

    If the product or the review hasn't been found, ``404`` status code is returned.

.. http:post:: /products/<product_id>/reviews/

  Allows you to add a new review to a product. 
  For each unique review, you can add :ref:`the following information<Review Information>`.

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
      - The id of a product to which you'd like to add a review.

  .. warning:: 

    This endpoint requires authentification token provided in the ``Authorization`` header.

  .. attention::

    This endpoint requires admin status.


  .. admonition:: Status Codes

    This endpoint can return ``404`` or ``403`` status code.

.. http:put:: /products/<product_id>/reviews/<review_id>

  Allows you to modify :ref:`a review's information<Review Information>`.

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
      - The id of a product that contains the review you'd like to modify.
    * - ``review_id``
      - ``int``
      - Yes
      - The id of the review you'd like to modify.

  .. warning:: 

    This endpoint requires authentification token provided in the ``Authorization`` header.

  .. attention::

    This endpoint requires admin status.


  .. admonition:: Status Codes

    This endpoint can return ``404`` or ``403`` status code. 

.. http:delete:: /products/<product_id>/reviews/<review_id>

  Allows you to remove a review.

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
      - The id of a product whose review you'd like to delete.
    * - ``review_id``
      - ``int``
      - Yes
      - The id of the review you'd like to delete.

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