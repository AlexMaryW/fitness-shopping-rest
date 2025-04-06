Foods
=====

This module allows you to create, view, search for, modify, and delete food items.

.. warning::
  All endpoints in this module require authentification token provided in the ``Authorization`` header.

Food Item Information
'''''''''''''''''''''

Each food item can be assigned the following information:

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
    - The food item's name, e.g. "carrot".
  * - Measure
    - ``str``
    - No
    - The food item's measure, e.g. grams or cup.
  * - Calories
    - ``float``
    - No
    - The amount of calories (kcal) in a food item.
  * - Protein
    - ``float``
    - No
    - The amount of protein in a food item, measured in grams.
  * - Carbohydrates
    - ``float``
    - No
    - The amount of carbohydrates in a food item, measured in grams.
  * - Fat
    - ``float``
    - No
    - The amount of fat in a food item, measured in grams.
  
.. note::
  The default value of each attribute is ``None``.

HTTP Endpoints
''''''''''''''

.. http:get:: /meals/<meal_id>/foods/

  Allows you to view all food items assigned to a meal.

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

  .. admonition:: Status Codes

    If the meal hasn't been found, ``404`` status code is returned.

.. http:get:: /meals/<meal_id>/foods/<food_id>

  Allows you to search for a food item.
  If successful, the endpoint returns :ref:`the food item's information<Food Item Information>`.

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
    * - ``food_id``
      - ``int``
      - Yes
      - The id the food item you're looking for.
  
  .. attention::  
    The request is successful only when:
      * both the ``meal_id`` and ``food_id`` you provided in the URL exist;
      * the meal you referenced contains the referenced the food item.

  .. admonition:: Status Codes

    If the meal or the food item hasn't been found, ``404`` status code is returned.

.. http:post:: /meals/<meal_id>/foods/

  Allows you to add a new food item. 
  For each unique food item, you can add :ref:`the following information<Food Item Information>`.

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

  .. admonition:: Status Codes

    This endpoint can return ``404`` or ``400`` status code.

.. http:put:: /meals/<meal_id>/foods/<food_id>

  Allows you to modify :ref:`a food item's information<Food Item Information>`.

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
      - The id of a meal that contains the food item you're looking for.
    * - ``food_id``
      - ``int``
      - Yes
      - The id the food item you're looking for.

  .. attention::  
    The request is successful only when:
      * both the ``meal_id`` and ``food_id`` you provided in the URL exist;
      * the meal you referenced contains the referenced the food item.

  .. admonition:: Status Codes

    If the meal or the food item hasn't been found, ``404`` status code is returned.    

.. http:delete:: /meals/<meal_id>/foods/<food_id>

  Allows you to remove a food item.

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
      - The id of a meal that contains the food item you're looking for.
    * - ``food_id``
      - ``int``
      - Yes
      - The id of the food item you're looking for.

  .. attention::  
    The request is successful only when:
      * both the ``meal_id`` and ``food_id`` you provided in the URL exist;
      * the meal you referenced contains the referenced the food item.

  .. admonition:: Status Codes
    
    This endpoint can return ``404`` or ``400`` status code.

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