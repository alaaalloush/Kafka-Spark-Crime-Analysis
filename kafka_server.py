from producer_server import ProducerServer


def run_kafka_server():
	# get the json file path
    input_file = "police-department-calls-for-service.json"

    producer = ProducerServer(
        input_file=input_file,
        topic="com.crime.police_call",
        bootstrap_servers="localhost:9092",
     #   client_id=""
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
