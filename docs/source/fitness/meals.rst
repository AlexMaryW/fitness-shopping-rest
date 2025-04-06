Meals
=====
This module allows you to create, view, search for, modify, and delete meals. 

.. warning::
  All endpoints in this module require authentification token provided in the ``Authorization`` header.

Meal Information
''''''''''''''''

Each meal is assigned the following information:

.. list-table::
  :widths: 25 10 10 30
  :header-rows: 1

  * - Attribute
    - Type
    - Required
    - Description
  * - Name
    - ``str``
    - Yes
    - The meal's name, e.g. chicken broth.
  * - Date
    - ``str``
    - Yes
    - The date a meal was created on. Defaults to today's date.
  * - ``user_id``
    - ``int``
    - Yes
    - The id of the currently logged in user is automatically assigned to the meal.


HTTP Endpoints
''''''''''''''

.. http:get:: /meals/

  Allows you to view all meals assigned to your ``user id``.


.. http:get:: /meals/<meal_id>

  Allows you to search for a meal.
  If successful, the endpoint returns the meal and :ref:`its information<Meal Information>`.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``meal_id``
      - ``int``
      - Yes
      - The id of a meal.
  
  .. attention::
    The request is successful only when the ``meal_id`` is assigned to your ``user_id``.

  .. admonition:: Status Codes

    If the meal hasn't been found, ``404`` status code is returned.


.. http:post:: /meals/

  Allows you to add a new meal. 
  For each unique meal, the app will add :ref:`the following information<Meal Information>`.

.. http:put:: /meals/<meal_id>

  Allows you to modify :ref:`a meal's information<Meal Information>` (except the ``user_id`` assigned to it). 

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``meal_id``
      - ``int``
      - Yes
      - The id of a meal you'd like to modify.

  .. attention::  
    The request is successful only when the ``meal_id`` is assigned to your ``user_id``.

  .. admonition:: Status Codes

    If the meal hasn't been found, ``404`` status code is returned.    

.. http:delete:: /meals/<meal_id>

  Allows you to remove a meal.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``meal_id``
      - ``int``
      - Yes
      - The id of a meal that you'd like to delete.

  .. attention::  
    The request is successful only when the ``meal_id`` is assigned to your ``user_id``.

  .. admonition:: Status Codes

    If the meal hasn't been found, ``404`` status code is returned. 

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