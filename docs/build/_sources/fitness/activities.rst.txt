Activities
==========

.. contents::


This module allows you to create, view, search for, modify, and delete activities. 

.. warning::
  All endpoints in this module require authentification token provided in the ``Authorization`` header.

Activity Information
''''''''''''''''

Each activity is assigned the following information:

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
    - The activity's name, e.g. yoga.
  * - Duration
    - ``float``
    - Yes
    - The duration of an activity in minutes, e.g. 30.00 minutes.
  * - Date
    - ``str``
    - Yes
    - The date an activity was created on. Defaults to today's date.
  * - Calories
    - ``float``
    - Yes
    - The amount of calories (kcal) burnt during an activity, e.g. 100.00 calories.
  * - ``user_id``
    - ``int``
    - Yes
    - The id of the currently logged in user is automatically assigned to the meal.


HTTP Endpoints
''''''''''''''

.. http:get:: /activities/

  Allows you to view all activities assigned to your ``user id``.


.. http:get:: /activities/<activity_id>

  Allows you to search for an activity.
  If successful, the endpoint returns the activity and :ref:`its information<Activity Information>`.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``activity_id``
      - ``int``
      - Yes
      - The id of an activity.
  
  .. attention::
    The request is successful only when the ``activity_id`` is assigned to your ``user_id``.

  .. admonition:: Status Codes

    If the activity hasn't been found, ``404`` status code is returned.


.. http:post:: /activities/

  Allows you to add a new activity. 
  For each unique activity, you can add :ref:`the following information<Activity Information>`.

.. http:put:: /activities/<activity_id>

  Allows you to modify :ref:`an activity's information<Activity Information>` (except the ``user_id`` assigned to it). 

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``activity_id``
      - ``int``
      - Yes
      - The id of an activity you'd like to modify.

  .. attention::  
    The request is successful only when the ``activity_id`` is assigned to your ``user_id``.

  .. admonition:: Status Codes

    If the activity hasn't been found, ``404`` status code is returned.    

.. http:delete:: /activities/<activity_id>

  Allows you to remove an activity.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``activity_id``
      - ``int``
      - Yes
      - The id of an activity that you'd like to delete.

  .. attention::  
    The request is successful only when the ``activity_id`` is assigned to your ``user_id``.

  .. admonition:: Status Codes

    If the activity hasn't been found, ``404`` status code is returned. 

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