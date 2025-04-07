from .models import ServiceRequest

class ServiceRequestService:
    
    @staticmethod
    def create_service_request(client_name, service_type):
        service_request = ServiceRequest.objects.create(
            client_name=client_name,
            service_type=service_type
        )
        return service_request

    @staticmethod
    def update_service_request_status(request_id, new_status):
        service_request = ServiceRequest.objects.get(id=request_id)
        service_request.status = new_status
        service_request.save()
        return service_request

    @staticmethod
    def delete_service_request(request_id):
        service_request = ServiceRequest.objects.get(id=request_id)
        service_request.delete()
        return service_request
