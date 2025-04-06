Messages
========

This module allows you to create, view, search for, and delete messages assigned to your application.

.. note::
  All endpoints in this module will create a new application if one does not already exist.


.. warning::
  All endpoints in this module require authentification token provided in the ``Authorization`` header.

Message Information
''''''''''''''''

Each message is assigned the following information:

.. list-table::
  :widths: 25 10 10 30
  :header-rows: 1

  * - Attribute
    - Type
    - Required
    - Description
  * - Date
    - ``str``
    - Yes
    - The date a message was created on. Defaults to today’s date.
  * - ``application_id``
    - ``int``
    - Yes
    - The id of the currently logged in user is automatically assigned to the message.
  * - ``is_user``
    - ``Boolean``
    - Yes
    - Designates whether the message was created by a human (``true``) or by an agent (``false``). Defaults to ``None``.
  * - ``text``
    - ``str``
    - Yes
    - The content of the message. Defaults to ``None``.

HTTP Endpoints
''''''''''''''

.. http:get:: /application/messages/

  Allows you to view all messages assigned to your application.


.. http:get:: /application/messages/<message_id>/

  Allows you to search for a message.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``message_id``
      - ``int``
      - Yes
      - The id of a message you'd like to view.
  

  .. admonition:: Status Codes

    If the message hasn't been found, ``404`` status code is returned.

.. http:post:: /application/messages/

  Allows you to add a new message. 
  The app will automatically assign date and ``application_id`` to the :ref:`message's information<Message Information>`.
  You can enter the message's ``text`` and ``is_user`` variable.
    
.. http:delete:: /application/messages/

  Allows you to remove all messages assigned to your application.


.. http:delete:: /application/messages/<message_id>/

  Allows you to remove a message assigned to your application.

  .. list-table:: Parameters
    :widths: 25 10 10 30
    :header-rows: 1

    * - Attribute
      - Type
      - Required
      - Description
    * - ``message_id``
      - ``int``
      - Yes
      - The id of a message you'd like to delete.

  .. admonition:: Status Codes
    
    If the message hasn't been found, ``404`` status code is returned.

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