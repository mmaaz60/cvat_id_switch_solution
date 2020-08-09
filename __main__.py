from parse_cvat_xml import ParseCVATXML


def main():
	xml_parser = ParseCVATXML("annotations.xml")
	xml_parser.parse_cvat_xml()
	xml_parser.dump_cvat_xml("test.xml")


if __name__ == "__main__":
	main()
