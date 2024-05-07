import threading
import socket

class BitcoinNode:
    PORT_MAINNET = 8333
    PORT_TESTNET = 18333

    def __init__(self):
        self.known_nodes = set()
        self.connections = {}  # Dictionary to store socket connections

    def discover_nodes(self, network='mainnet'):
        # Defines a list of known or seed nodes that can be used to initiate the connection.
        seed_nodes_mainnet = [
            ("seed.bitcoin.sipa.be", self.PORT_MAINNET),
            ("dnsseed.bluematt.me", self.PORT_MAINNET),
            ("dnsseed.bitcoin.dashjr.org", self.PORT_MAINNET),
            ("seed.bitcoinstats.com", self.PORT_MAINNET),
            ("terra.ignorelist.com", self.PORT_MAINNET),
            # Add more seed nodes if necessary
        ]
        
        seed_nodes_testnet = [
            # Define seed nodes for testnet
            ("testnet-seed.bitcoin.petertodd.org", self.PORT_TESTNET),
            ("testnet-seed.bluematt.me", self.PORT_TESTNET),
            ("seed.testnet.bitcoin.sprovoost.nl", self.PORT_TESTNET)
            # Add more testnet seed nodes if necessary
        ]
        
        # Choose seed nodes based on the network
        seed_nodes = seed_nodes_mainnet if network == 'mainnet' else seed_nodes_testnet

        # Iterates over the seed nodes and tries to connect to each of them.
        for node_address, node_port in seed_nodes:
            self.connect_to_node(node_address, node_port)

    def connect_to_node(self, ip, port):
        try:
            # Create a TCP socket to connect to the node.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the connection.
            sock.settimeout(3)
            # It attempts to connect to the node using its IP address and port.
            sock.connect((ip, port))
            # If the connection is successful, it adds the node to the list of known nodes.
            print(f"Connected to node: {ip}:{port}")
            # Add a node to the list of known nodes
            self.known_nodes.add((ip, port))
            # Store the socket connection in the connections dictionary
            self.connections[(ip, port)] = sock

        except socket.timeout:
            # If the timeout is exceeded, print an error message.
            print(f"Connection error: Timeout connecting to {ip}:{port}")
        except ConnectionRefusedError:
            # If the node refuses the connection, print an error message.
            print(f"Connection error: Connection refused by {ip}:{port}")
        except Exception as e:
            # If there is any other error while trying to connect to the node, print a generic error message.
            print(f"Connection error: {e}")

    def close_all_connections(self):
        # Close all socket connections
        for sock in self.connections.values():
            sock.close()
            print("Connection closed")
        self.connections.clear()

    def send_message(self, message, ip, port):
        # Send a message to a connected Bitcoin node
        try:
            sock = self.connections.get((ip, port))
            if sock is not None:
                sock.sendall(message.encode())
                print("Message sent successfully")
            else:
                print("Connection not found for the specified node")
        except socket.timeout:
            print(f"Connection error: Timeout connecting to {ip}:{port}")
        except ConnectionRefusedError:
            print(f"Connection error: Connection refused by {ip}:{port}")
        except Exception as e:
            print(f"Connection error: {e}")

    def receive_message(self):
        # Continuously listen to responses from connected nodes
        while True:
            for sock in self.connections.values():
                try:
                    # Receive data from the connection socket
                    data = sock.recv(1024)
                    if data:
                        # Process the received data (you can define the logic according to the Bitcoin protocol)
                        print("Message received:", data)
                except Exception as e:
                    # Handle any errors that occur during message reception
                    print("Error receiving message:", e)

    def start_message_receiver_thread(self):
        # Handle incoming Bitcoin messages
        receiver_thread = threading.Thread(target=self.receive_message)
        receiver_thread.daemon = True
        receiver_thread.start()

# Connect to other nodes, exchange messages, etc.
if __name__ == "__main__":
    node = BitcoinNode()

    try:
        node.discover_nodes(network="testnet")
        node.start_message_receiver_thread()

        # Testing if we are communicating with the nodes on the network
        # Send a release message to the first node in the list of known nodes
        if node.known_nodes:
            first_node = list(node.known_nodes)[0]
            node.send_message("version", first_node[0], first_node[1])
        else:
            print("No known nodes were found.")

        while True:
            pass

    except KeyboardInterrupt:
        print("KeyboardInterrupt detected. Closing all connections.")
    except socket.error as se:
        print(f"Socket error: {se}. Closing all connections.")
    except Exception as e:
        print(f"An error occurred: {e}. Closing all connections.")
    finally:
        node.close_all_connections()
