

class TrackFrames:
	def __init__(self, frame_no, xtl, ytl, xbr, ybr, outside, occluded, keyframe):
		self.frame_no = frame_no
		self.xtl = xtl
		self.ytl = ytl
		self.xbr = xbr
		self.ybr = ybr
		self.outside = outside
		self.occluded = occluded
		self.keyframe = keyframe


class CVATTrack:
	def __init__(self, track_id, track_label, track_shape):
		self.id = track_id
		self.label = track_label
		self.shape = track_shape
		self.track_frames = []
		
	def add_frame(self, frame_no, xtl, ytl, xbr, ybr, outside, occluded, keyframe):
		self.track_frames.append(TrackFrames(frame_no, xtl, ytl, xbr, ybr, outside, occluded, keyframe))
