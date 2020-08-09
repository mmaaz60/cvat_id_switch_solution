import xml.etree.ElementTree as ET
from cvat_track import CVATTrack
import pickle
from xml_writer import XMLWriter


class ParseCVATXML:
    def __init__(self, cvat_xml_path):
        self.cvat_xml_path = cvat_xml_path
        self.cvat_tracks = {}

    def parse_cvat_xml(self):
        tree = ET.parse(self.cvat_xml_path)
        root = tree.getroot()
        track_list = [child for child in root if child.tag == "track"]
        for tracks in track_list:
            track_id = int(tracks.attrib['id'])
            track_label = tracks.attrib['label']

            cvat_track = CVATTrack(track_id, track_label, "box")

            track_frames = [child.attrib for child in tracks if child.tag == "box"]
            for attrib in track_frames:
                frame_no = int(attrib['frame'])
                xtl = float(attrib['xtl'])
                ytl = float(attrib['ytl'])
                xbr = float(attrib['xbr'])
                ybr = float(attrib['ybr'])
                outside = attrib['outside']
                occluded = attrib['occluded']
                keyframe = attrib['keyframe']

                cvat_track.add_frame(frame_no, xtl, ytl, xbr, ybr, outside, occluded, keyframe)

            self.cvat_tracks[track_id] = cvat_track

    def get_cvat_tracks(self):
        return self.cvat_tracks

    def dump_cvat_tracks_as_pkl(self, file_path):
        with open(file_path, "wb") as f:
            pickle.dump(self.cvat_tracks, f)

    def load_cvat_tracks_from_pkl_file(self, file_path):
        with open(file_path, "rb") as f:
            self.cvat_tracks = pickle.load(f)

    def swap_track_labels(self, track_ids, frame_no):
        id1, id2 = track_ids
        track_1, track_2 = self.cvat_tracks[id1], self.cvat_tracks[id2]

        new_track_1 = CVATTrack(track_1.id, track_1.label, track_1.shape)
        new_track_2 = CVATTrack(track_2.id, track_2.label, track_2.shape)

        for track_frame in track_1.track_frames:
            if track_frame.frame_no < frame_no:
                new_track_1.add_frame(track_frame.frame_no, track_frame.xtl, track_frame.ytl, track_frame.xbr,
                                      track_frame.ybr, track_frame.outside, track_frame.occluded, track_frame.keyframe)
            else:
                new_track_2.add_frame(track_frame.frame_no, track_frame.xtl, track_frame.ytl, track_frame.xbr,
                                      track_frame.ybr, track_frame.outside, track_frame.occluded, track_frame.keyframe)

        for track_frame in track_2.track_frames:
            if track_frame.frame_no < frame_no:
                new_track_2.add_frame(track_frame.frame_no, track_frame.xtl, track_frame.ytl, track_frame.xbr,
                                      track_frame.ybr, track_frame.outside, track_frame.occluded, track_frame.keyframe)
            else:
                new_track_1.add_frame(track_frame.frame_no, track_frame.xtl, track_frame.ytl, track_frame.xbr,
                                      track_frame.ybr, track_frame.outside, track_frame.occluded, track_frame.keyframe)
        new_track_1.track_frames.sort(key=lambda x: x.frame_no)
        new_track_2.track_frames.sort(key=lambda x: x.frame_no)
        self.cvat_tracks[id1], self.cvat_tracks[id2] = new_track_1, new_track_2

    def dump_cvat_xml(self, xml_source, xml_destination):
        xml_object = XMLWriter("annotations")
        xml_object.read_from_file(xml_source)
        xml_object.remove_tracks()

        for i in range(2):
            cvat_track = self.cvat_tracks[i]
            xml_object.add_track(cvat_track)

        xml_object.dump_xml(xml_destination)
