Food Archetypes
===============

This module allows you to create, view, search for, modify, and delete food archetypes.

.. warning::
  All endpoints in this module require authentification token provided in the ``Authorization`` header.

Food Archetype Information
'''''''''''''''''''''

Each food archetype can be assigned the following information:

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
    - The food archetype's name, e.g. "carrot".
  * - Measure
    - ``str``
    - No
    - The food archetype's measure, e.g. grams or cup.
  * - Calories
    - ``float``
    - No
    - The amount of calories (kcal) in a food archetype.
  * - Protein
    - ``float``
    - No
    - The amount of protein in a food archetype, measured in grams.
  * - Carbohydrates
    - ``float``
    - No
    - The amount of carbohydrates in a food archetype, measured in grams.
  * - Fat
    - ``float``
    - No
    - The amount of fat in a food archetype, measured in grams.
  
.. note::
  The default value of each attribute is ``None``.

HTTP Endpoints
''''''''''''''

.. http:get:: /foods/

  Allows you to view all food archetypes.

  .. admonition:: Status Codes

    If the food archetype hasn't been found, ``404`` status code is returned.

.. http:get:: foods/<food_id>

  Allows you to search for a food archetype.
  If successful, the endpoint returns :ref:`the food archetype's information<Food Archetype Information>`.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``food_id``
      - ``int``
      - Yes
      - The id the food archetype you're looking for.

  .. admonition:: Status Codes

    If the food archetype hasn't been found, ``404`` status code is returned.

.. http:post:: /foods/

  Allows you to add a new food archetype. 
  For each unique food archetype, you can add :ref:`the following information<Food Archetype Information>`.

  .. attention::
    This endpoint requires admin status.

  .. admonition:: Status Codes

    This endpoint can return ``403`` or ``400`` status code.

.. http:put:: /foods/

  Allows you to replace a food archetype with a new one.
  You can add :ref:`the following information<Food Archetype Information>` for your new food archetype.

  .. attention::
    This endpoint requires admin status.

  .. admonition:: Status Codes

    This endpoint can return ``403`` or ``400`` status code.   

.. http:put:: /foods/<food_id>

  Allows you to modify :ref:`a food archetype's information<Food Archetype Information>`.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``food_id``
      - ``int``
      - Yes
      - The id the food archetype you're looking for.

  .. attention::
    This endpoint requires admin status.
    
  .. admonition:: Status Codes

    This endpoint can return ``403``, ``404``, or ``400`` status code. 

.. http:delete:: foods/<food_id>

  Allows you to remove a food archetype.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``food_id``
      - ``int``
      - Yes
      - The id the food archetype you're looking for.

  .. attention::
    This endpoint requires admin status.

  .. admonition:: Status Codes
    
    This endpoint can return ``403`` or ``404`` status code.

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