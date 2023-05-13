import grpc
import subprocess
from concurrent import futures
import remote_control_pb2
import remote_control_pb2_grpc

class RemoteControlServicer(remote_control_pb2_grpc.RemoteControlServicer):
    def ExecuteCommand(self, request, context):
        command = request.command
        try:
            result = subprocess.check_output(command, shell=True)
            return remote_control_pb2.CommandResponse(result=result.decode())
        except subprocess.CalledProcessError as e:
            return remote_control_pb2.CommandResponse(error=str(e))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    remote_control_pb2_grpc.add_RemoteControlServicer_to_server(RemoteControlServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

