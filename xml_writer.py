import xml.etree.ElementTree as ET


class XMLWriter:
    def __init__(self, root):
        self.root = ET.Element(root)
        self.tree = ET.ElementTree(self.root)

    def read_from_file(self, xml_file_path):
        self.tree = ET.parse(xml_file_path)
        self.root = self.tree.getroot()

    def add_xml_element(self, parent, element):
        if self.root.tag == parent:
            self.root.append(element)
        else:
            for e in self.root.iter(parent):
                e.append(element)
                break

    def add_track(self, cvat_track):
        track = ET.Element("track")
        track.set("id", str(cvat_track.id))
        track.set("label", str(cvat_track.label))

        for track_frame in cvat_track.track_frames:
            box = ET.Element("box")
            box.set("frame", str(track_frame.frame_no))
            box.set("outside", str(track_frame.outside))
            box.set("occluded", str(track_frame.occluded))
            box.set("keyframe", str(track_frame.keyframe))
            box.set("xtl", str(track_frame.xtl))
            box.set("ytl", str(track_frame.ytl))
            box.set("xbr", str(track_frame.xbr))
            box.set("ybr", str(track_frame.ybr))
            track.append(box)

        self.root.append(track)

    def remove_tracks(self):
        tracks = self.root.findall("track")
        for track in tracks:
            self.root.remove(track)

    def dump_xml(self, xml_file_path):
        def indent(elem, level=0):
            i = "\n" + level * "  "
            if len(elem):
                if not elem.text or not elem.text.strip():
                    elem.text = i + "  "
                if not elem.tail or not elem.tail.strip():
                    elem.tail = i
                for elem in elem:
                    indent(elem, level + 1)
                if not elem.tail or not elem.tail.strip():
                    elem.tail = i
            else:
                if level and (not elem.tail or not elem.tail.strip()):
                    elem.tail = i

        indent(self.root)
        self.tree.write(xml_file_path, encoding="utf-8", xml_declaration=True)
