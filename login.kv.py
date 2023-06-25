Screen:
    
    MDCard:
        size_hint: None, None
        size: 300, 400
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

        MDLabel:
            id: welcome_label
            text: "WELCOME"
            font_size: 40
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

        MDTextFieldRound:
            id: user
            hint_text: "username"
            icon_right: "account"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}

        MDTextFieldRound:
            id: password
            hint_text: "password"
            icon_right: "eye-off"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
            password: True

        MDRoundFlatButton:
            text: "LOG IN"
            font_size: 12
            pos_hint: {"center_x": 0.5}
            on_press: app.logger()

        MDRoundFlatButton:
            text: "CLEAR"
            font_size: 12
            pos_hint: {"center_x": 0.5} 
            on_press: app.clear()           

        Widget:
            size_hint_y: None
            height: 10