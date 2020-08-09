from parse_cvat_xml import ParseCVATXML
import configparser


def main():
	config = configparser.ConfigParser()
	config.read("config.ini")

	xml_source = config['data']['input_cvat_xml_path']
	xml_destination = config['data']['output_cvat_xml_path']

	xml_parser = ParseCVATXML(xml_source)
	xml_parser.parse_cvat_xml()

	track_ids_list = config['swap_labels']['track_ids_list'].split(':')
	frame_no_list = config['swap_labels']['frame_no_list'].split(':')

	for track_ids, frame_no in zip(track_ids_list, frame_no_list):
		track_ids = [int(i) for i in track_ids.split(',')]
		xml_parser.swap_track_labels(track_ids, int(frame_no))

	xml_parser.dump_cvat_xml(xml_source, xml_destination)


if __name__ == "__main__":
	main()
