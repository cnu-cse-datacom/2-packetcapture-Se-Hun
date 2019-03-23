import socket
import struct

def parsing_ethernet_header(data):
	ethernet_header = struct.unpack("!6c6c2s", data)
	ether_src = convert_ethernet_address(ethernet_header[0:6])
	ether_dest = convert_ethernet_address(ethernet_header[6:12])
	ip_header = "0x"+ethernet_header[12].hex()

	print("=========ethernet header=========")
	print("src_mac_address:", ether_src)
	print("dest_mac_address:", ether_dest)
	print("ip_version", ip_header)

def parsing_ip_header(data):
	ip_header = struct.unpack("!2B3H2BH4B4B", data)
	ip_version = ip_header[0] >> 4 # 앞의 4비트만 갖게 해야함
	ip_length = ip_header[0] & 15 # 뒤의 4비트만 갖게 해야함
	dsc = ip_header[1] >> 2 # 앞의 6비트만 가지게 해야함
	ecn = ip_header[1] & 3 # 뒤의 2비트만 갖게 해야함
	total_length = ip_header[2]
	identification = ip_header[3]
	flags = hex(ip_header[4]) # 0x형태로 만들어주어야함
	reserved_bit = ip_header[4] >> 15 # 맨 첫번째 한 비트만 가지게 해야함
	not_fragments = (ip_header[4] >> 14) & 1 # 앞에서 두번째의 한 비트만 가지게 해주어야함
	fragments = (ip_header[4] >> 13) & 1 # 앞에서 세번째의 한 비트만 가지게 해주어야함
	fragments_offset = ip_header[4] & 16383 # 뒤의 13비트만 가지게!! 앞의 3비트 잘라야함
	time_to_live = ip_header[5]
	protocol = ip_header[6]
	header_checksum = ip_header[7]
	ip_src = convert_ip_address(ip_header[8:12])
	ip_dest = convert_ip_address(ip_header[12:16])

	print("=========ip_header=========")
	print("ip_version:", ip_version)
	print("ip_Length:", ip_length)
	print("differentiated_service_codepoint:", dsc)
	print("explicit_congestion_notification:", ecn)
	print("total_length:", total_length)
	print("identification:", identification)
	print("flags:", flags)
	print(">>>reserved_bit:", reserved_bit)
	print(">>>not_fragments:", not_fragments)
	print(">>>fragments:", fragments)
	print(">>>fragments_offset", fragments_offset)
	print("Time to live:", time_to_live)
	print("protocol:", protocol)
	print("header checksum:", header_checksum)
	print("source_ip_address:", ip_src)
	print("dest_ip_address:", ip_dest)
	# ip_header함수 마지막에 return으로 프로토콜 값을 주어야함!!
	return protocol

def parsing_tcp_header(data):
	tcp_header = struct.unpack("!2H2I4H", data)
	src_port = tcp_header[0]
	dst_port = tcp_header[1]
	seq_num = tcp_header[2]
	ack_num = tcp_header[3]
	header_len = tcp_header[4] >> 12 # 앞의 4비트만 가지도록
	flags = tcp_header[4] & 4095 #12비트만 가지도록
	reserved = flags >> 9 # 3비트
	nonce = (flags >> 8) & 1 # 1bit
	cwr = (flags >> 7) & 1
	echo = (flags >> 6) & 1
	urgent = (flags >> 5) & 1
	ack = (flags >> 4) & 1
	push = (flags >> 3) & 1
	reset = (flags >> 2) & 1
	syn = (flags >> 1) & 1
	fin = flags & 1
	window_size_value = tcp_header[5]
	checksum = tcp_header[6]
	urgent_pointer = tcp_header[7]
	
	print("=========tcp_header=========")
	print("src_port:", src_port)
	print("dst_port", dst_port)
	print("seq_num:", seq_num)
	print("ack_num:", ack_num)
	print("header_len:", header_len)
	print("flags:", flags)
	print(">>>reserved:", reserved)
	print(">>>nonce:", nonce)
	print(">>>cwr:", cwr)
	print(">>>echo:", echo)
	print(">>>urgent:", urgent)
	print(">>>ack:", ack)
	print(">>>push:", push)
	print(">>>reset:", reset)
	print(">>>syn:", syn)
	print(">>>fin:", fin)
	print("window_size_value:", window_size_value)
	print("checksum:", checksum)
	print("urgent_pointer:", urgent_pointer)

def parsing_udp_header(data):
	udp_header = struct.unpack("!4H", data)
	src_port = udp_header[0]
	dst_port = udp_header[1]
	leng = udp_header[2]
	header_checksum = udp_header[3]

	print("=========udp_header=========")
	print("src_port:", src_port)
	print("dst_port:", dst_port)
	print("leng:", leng)
	print("header_checksum:", header_checksum)

def convert_ethernet_address(data):
	ethernet_addr = list()
	for i in data:
		ethernet_addr.append(i.hex())
	ethernet_addr = ":".join(ethernet_addr)
	return ethernet_addr

def convert_ip_address(data):
	ip_addr = list()
	for i in data:
		ip_addr.append(str(i))
	ip_addr = ".".join(ip_addr)
	return ip_addr

recv_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x800))

print("<<<<<<Packet Capture Start>>>>>>")

while True:
	print("<<<<<<New Packet>>>>>>")
	protocol_number = 0
	data = recv_socket.recvfrom(65565)
	parsing_ethernet_header(data[0][0:14])
	protocol_number = parsing_ip_header(data[0][14:34])
	#if문으로 tcp인지, udp인지 한번 확인해줘야함.
	if protocol_number == 6:
		parsing_tcp_header(data[0][34:54])
	else: #udp : 17번
		parsing_udp_header(data[0][34:42])
		

