from fields._base import FieldBase
from fields.barcode import Barcode
from fields.box_number import BoxNumber
from fields.string import String


class Header(FieldBase):
    stations = {
        "Red1": 1,
        "Red2": 2,
        "Red3": 3,
        "Blue1": 4,
        "Blue2": 5,
        "Blue3": 6
    }

    positions = [
        "Red 1",
        "Red 2",
        "Red 3",
        "Blue 1",
        "Blue 2",
        "Blue 3"
    ]

    def __init__(self, match, pos, team=None, eventName = None):
        super().__init__()
        self.match = match
        self.pos = pos
        self.team = team
        self.event = eventName

    def draw(self, canvas, x_pos, y_pos, config):
        if self.event is None:
            self.event = config['event']
        String("OT Robotics", font_size=0.25).draw(canvas, 0.05 + config["marker_size"],
                                                   0.05 + config["marker_size"], config)
        String(self.event, font_size=3.0 / 32).draw(canvas, 0.125 + config["marker_size"],
                                                         0.3 + config["marker_size"], config)
        if self.team is not None:
            team = "(" + str(self.team) + ")"
            pos = self.pos
        else:
            pos = self.positions[self.pos]
            team = ""
        String("Match " + str(self.match) + "    " + pos + team + "    Scout: _______", font_size=0.25) \
            .draw(canvas, 0.125 + config["marker_size"], 7.0 / 16 + config["marker_size"], config)

        match_pos_string = str(self.match)
        while len(match_pos_string) < 3:
            match_pos_string = "0" + match_pos_string

        if self.team is not None:
            match_pos_string += str(self.stations[self.pos])
        else:
            match_pos_string += str(self.pos)


        barcode = Barcode("-EncodedMatchData", int(match_pos_string))
        barcode.set_id("encoded_match_data")
        barcode_x = 8.5 - config["marker_size"]
        barcode_y = config["marker_size"]
        barcode.draw(canvas, barcode_x, barcode_y, config)

        team_num = BoxNumber("Team Number")
        team_num_x = config["x_pos"] + config["marker_size"]
        team_num_y = 1
        team_num.set_id("team_num")
        team_num.draw(canvas, team_num_x, team_num_y, config)

        box_bardcode_info = [
            {
                "type": barcode.get_type(),
                "id": barcode.get_id(),
                "options": barcode.get_info(),
                "x_pos": barcode_x,
                "y_pos": barcode_y,
                "height": barcode.get_height(config)
            },
            {
                "type": team_num.get_type(),
                "id": team_num.get_id(),
                "options": team_num.get_info(),
                "x_pos": team_num_x,
                "y_pos": team_num_y,
                "height": team_num.get_height(config)
            }
        ]

        if self.team is not None:
            team_num_encode = Barcode("-EncodedTeamNumber", int(self.team))
            team_num_encode_x = barcode_x - 3
            team_num_encode_y = barcode_y
            team_num_encode.set_id("team_number_encoded")
            team_num_encode.draw(canvas, team_num_encode_x, team_num_encode_y, config)
            box_bardcode_info.append({
                "type": team_num_encode.get_type(),
                "id": team_num_encode.get_id(),
                "options": team_num_encode.get_info(),
                "x_pos": team_num_encode_x,
                "y_pos": team_num_encode_y,
                "height": team_num_encode.get_height(config)
            })

        return self.get_height(config), box_bardcode_info

    def get_height(self, config):
        return BoxNumber("Team Number").get_height(config)
