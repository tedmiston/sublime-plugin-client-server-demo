from flask import Response, jsonify


class JsonResponse(Response):
    """Automatically jsonify dict return values for views."""
    @classmethod
    def force_type(cls, rv, environ=None):
        if isinstance(rv, dict):
            rv = jsonify(rv)
        return super(JsonResponse, cls).force_type(rv, environ)
