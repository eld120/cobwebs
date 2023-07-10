from datetime import date

from rest_framework import mixins


class CustomerSingleObjectMixin(mixins.CreateModelMixin):
    def perform_create(self, serializer):
        print(serializer.validated_data)
        serializer.save(
            start_date=date.today().strftime("%Y-%m-%d"), created_by=self.request.user
        )
