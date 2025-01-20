head="""
    <script>
           function top_open_control() {
                var panel = document.querySelector('#gs_top_control_panel');
                if (panel.classList.value.includes("open") === false) {
                panel.classList = '#gs_top_control_panel'
                panel.classList.toggle('open');
                console.log('clicked')
                } else {
                panel.classList = '#gs_top_control_panel'
                console.log('panel is open, closing')
                };
                };
            function left_open_control() {
                var panel = document.querySelector('#gs_left_control_panel');
                var left_bar = document.querySelector('#gs_left_bar');
                var left_btn = document.querySelector('#left_control_btn');
                var split_json = []
                var out_json = []
                split_json = panel.classList.value.split(' ')
                console.log(split_json.length)
                if (panel.classList.value.includes("open") === false) {
                panel.classList = '#gs_left_control_panel'
                left_bar.classList = '#gs_left_bar'
                left_btn.classList = '#left_control_btn'
                panel.classList.toggle('open');
                left_bar.classList.toggle('open');
                left_btn.classList.toggle('open');
                console.log('clicked')
                } else {
                panel.classList = '#gs_left_control_panel'
                left_bar.classList = '#gs_left_bar'
                left_btn.classList = '#left_control_btn'
                console.log('panel is open, closing')
                };
                };
            function right_open_control() {
                var panel = document.querySelector('#gs_right_control_panel');
                var right_bar = document.querySelector('#gs_right_bar');
                var right_btn = document.querySelector('#right_control_btn');
                var split_json = []
                var out_json = []
                split_json = panel.classList.value.split(' ')
                console.log(split_json.length)
                if (panel.classList.value.includes("open") === false) {
                panel.classList = '#gs_right_control_panel'
                right_bar.classList = '#gs_right_bar'
                right_btn.classList = '#right_control_btn'
                panel.classList.toggle('open');
                right_bar.classList.toggle('open');
                right_btn.classList.toggle('open');
                console.log('clicked')
                } else {
                panel.classList = '#gs_right_control_panel'
                right_bar.classList = '#gs_right_bar'
                right_btn.classList = '#right_control_btn'
                console.log('panel is open, closing')
                };
                };
        </script>
      """ 
css="""
#gs_top_control_panel {
    position: fixed;
    right: 100%;
    z-index: 999999;
    width: 40%;
    top: 50px;
    box-shadow: 0 0 12px 0px black;
    transition: right 0.5s ease;
    }
#gs_top_control_panel.open {
    right: 60%;
    }
#gs_left_control_panel {
    position: fixed;
    left: -110%;
    z-index: 9999;
    width: 330px;
    top: 50px;
    box-shadow: black 0px 0px 12px 0px;
    transition: left 0.5s linear;
    }
#gs_left_control_panel.open {
    left: 0%;
    }
#gs_right_control_panel {
    position: fixed;
    right: -110%;
    z-index: 9999;
    width: 330px;
    top: 50px;
    box-shadow: black 0px 0px 12px 0px;
    transition: right 0.5s linear;
    }
#gs_right_control_panel.open {
    right: 0%;
    }
#top_control_btn {
    height: 20px;
    padding: 10px;
    cursor: pointer;
    border-radius: 5px;
    color: white;
    position: fixed;
    z-index: 9999999999999999;
    top: 5px;
    left: 10px;
    background: #1e293b;
    height: fit-content;
    width: fit-content; 
}
#left_control_btn {
    padding: 10px;
    cursor: pointer;
    border-radius: 5px;
    color: white;
    position: fixed;
    z-index: 2147483647;
    top: 70px;
    left: -20px;
    background: rgb(30, 41, 59);
    height: fit-content;
    width: fit-content;
    transition: left 0.5s linear;
    transform: rotate(90deg);
}
#left_control_btn.open{
    left:340px;
}
#right_control_btn {
    padding: 10px;
    cursor: pointer;
    border-radius: 5px;
    color: white;
    position: fixed;
    z-index: 2147483647;
    top: 70px;
    right: -20px;
    background: rgb(30, 41, 59);
    height: fit-content;
    width: fit-content;
    transition: right 0.5s linear;
transform: rotate(270deg);
}
#right_control_btn.open{
    right:340px;
}
#gs_top_bar {
    height: 50px;
    width: 100%;
    position: fixed;
    background: #185991;
    top: 0px;
    left: 0px;
    z-index: 99999;
    }
#gs_top_bar.open {
    left:350px;
}
#gs_left_bar {
    height: 100%;
    width: 360px;
    position: fixed;
    background: rgb(24, 89, 145);
    top: 0px;
    left: -370px;
    z-index: 9999;
    transition: left 0.5s linear;
}
#gs_left_bar.open {
    left: 0px;
}
#gs_right_bar {
    height: 100%;
    width: 360px;
    position: fixed;
    background: rgb(24, 89, 145);
    top: 0px;
    right: -360px;
    z-index: 9999;
    transition: right 0.5s linear;
}
#gs_right_bar.open {
    right: 0px;
}
  """
topbar="""<div id='gs_top_bar'><div id='top_control_btn' onclick='top_open_control()'>Controls</div></div>"""
leftbar="""<div id='gs_left_bar'><div id='left_control_btn' onclick='left_open_control()'>Controls</div></div>"""
rightbar="""<div id='gs_right_bar'><div id='right_control_btn' onclick='right_open_control()'>Controls</div></div>"""
