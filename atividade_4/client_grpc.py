import grpc
import click
import remote_control_pb2
import remote_control_pb2_grpc

@click.command()
@click.option("--host", default="localhost", help="Server host")
@click.option("--port", default=50051, help="Server port")
def run(host, port):
    with grpc.insecure_channel(f"{host}:{port}") as channel:
        stub = remote_control_pb2_grpc.RemoteControlStub(channel)
        while True:
            command = click.prompt("Enter command")
            if command == "exit":
                break
            request = remote_control_pb2.CommandRequest(command=command)
            response = stub.ExecuteCommand(request)
            if response.error:
                print(f"Error: {response.error}")
            else:
                print(response.result)

if __name__ == "__main__":
    run()
