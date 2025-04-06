User Module
===========

This module allows you to create, view, search for, modify, and delete your account.


User Information
''''''''''''''''

Each user can be assigned the following information:

.. list-table::
  :widths: 25 10 10 30
  :header-rows: 1

  * - Attribute
    - Type
    - Required
    - Description
  * - Username
    - ``str``
    - Yes
    - Your username for the app. 
  * - Password
    - ``str``
    - Yes
    - Your passowrd for the app. The app uses the SHA-256 algorithm to hash the passwords.
  * - ``FirstName``
    - ``str``
    - No
    - Your given name.
  * - ``LastName``
    - ``str``
    - No
    - Your surname.
  * - ``GoalDailyCalories``
    - ``float``
    - No
    - The amount of calories (kcal) you'd like to consume every day.
  * - ``GoalDailyProtein``
    - ``float``
    - No
    - The amount of protein you'd like to consume every day.
  * - ``GoalDailyCarbohydrates``
    - ``float``
    - No
    - The amount of carbohydrates you'd like to consume every day.
  * - ``GoalDailyFat``
    - ``float``
    - No
    - The amount of fat you'd like to consume every day.
  * - ``GoalDailyActivity``
    - ``float``
    - No
    - The amount of time you'd like to dedicate to moving your body every day.
  
.. note::
  The default value of optional attributes is ``None``.

HTTP Endpoints
''''''''''''''

.. http:get:: /users/

  Allows you to view all user accounts.

  .. warning:: 

    This endpoint requires authentification token provided in the ``Authorization`` header.

  .. attention::

    This endpoint requires admin status.

  .. admonition:: Status Codes

    This endpoint can return ``401`` status code.


.. http:get:: /users/<username>

  Allows you to view your :ref:`user information<User Information>`.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``username``
      - ``str``
      - Yes
      - Your username.

  .. warning:: 

    This endpoint requires authentification token provided in the ``Authorization`` header.

  .. admonition:: Status Codes

    This endpoint can return ``401`` or ``404`` status code.

.. http:post:: /users/

  Allows you to create an account.
  For each unique account, you can add :ref:`the following information<User Information>`.


  .. admonition:: Status Codes

    This endpoint can return ``400``, ``409``, or ``403`` status code.

.. http:put:: /users/<username>

  Allows you to modify your :ref:`user information<User Information>`.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``username``
      - ``str``
      - Yes
      - Your username.

  .. warning:: 

    This endpoint requires authentification token provided in the ``Authorization`` header.

  .. attention::

    This endpoint requires admin status.


  .. admonition:: Status Codes

    This endpoint can return ``404`` or ``401`` status code. 

.. http:delete:: /users/<username>

  Allows you to remove your account.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``username``
      - ``str``
      - Yes
      - Your username.

  .. warning:: 

    This endpoint requires authentification token provided in the ``Authorization`` header.

  .. attention::

    This endpoint requires admin status.


  .. admonition:: Status Codes

    This endpoint can return ``404`` or ``401`` status code.

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