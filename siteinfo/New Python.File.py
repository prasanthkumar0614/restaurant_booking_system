{% extends "base.html" %}
{% block content %}
<h2>Restaurant Info</h2>

{% if profile %}
    {% if profile.logo %}
        <img src="{{ profile.logo.url }}" alt="logo" width="80" height="80" style="border-radius:50%; object-fit:cover; margin-bottom:16px;">
    {% endif %}

    <h3>{{ profile.name }}</h3>
    {% if profile.tagline %}<p><em>{{ profile.tagline }}</em></p>{% endif %}
    {% if profile.description %}<p>{{ profile.description }}</p>{% endif %}

    <p>📍 <strong>Address:</strong> {{ profile.address }}</p>
    <p>📞 <strong>Contact:</strong> {{ profile.contact_number }}</p>
    <p>✉️ <strong>Email:</strong> {{ profile.email }}</p>
    <p>⏰ <strong>Hours:</strong> {{ profile.opening_time }} – {{ profile.closing_time }}</p>
{% else %}
    <p>Restaurant info not added yet. Add it from the Django admin panel.</p>
{% endif %}
{% endblock %}