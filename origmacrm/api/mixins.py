from datetime import date

from rest_framework import mixins


class CustomerSingleObjectMixin(mixins.CreateModelMixin):
    def perform_create(self, serializer):
        serializer.save(
            start_date=date.today().strftime("%Y-%m-%d"), created_by=self.request.user
        )
