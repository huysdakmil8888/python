from rest_framework.routers import DefaultRouter
from rest_framework.permissions import IsAuthenticated

class AuthenticatedRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trailing_slash = '/?'

    def get_default_basename(self, viewset):
        """
        Given a viewset, return the default base name for the routes.
        This can be overridden in subclasses, for example to add
        a 'list-' prefix to views that return a list of objects.
        """
        queryset = getattr(viewset, 'queryset', None)

        assert queryset is not None, '`basename` argument not specified, and could ' \
                                     'not automatically determine the name from the viewset, as ' \
                                     'it does not have a `.queryset` attribute.'

        return queryset.model._meta.object_name.lower()

    def get_default_actions(self):
        return ['list', 'create', 'retrieve', 'update', 'partial_update', 'destroy']

    def get_default_view_name(self, action_keys):
        return '-'.join(action_keys)

    def get_urls(self):
        """
        Use the registered viewsets to generate a list of URL patterns.
        """
        ret = []

        for prefix, viewset, basename in self.registry:
            # Determine any `@action` or `@link` decorated methods on the viewset
            routes = self.get_routes(viewset)
            for route in routes:
                mapping = self.get_method_map(viewset, route.mapping)
                if not mapping:
                    continue

                # Apply the `IsAuthenticated` permission class to all views
                for method in mapping.values():
                    method.permission_classes = [IsAuthenticated]

                # Set URL pattern
                regex = route.url.replace('{basename}', basename)
                ret.append(path(regex, include(route.mapping)))

        return ret