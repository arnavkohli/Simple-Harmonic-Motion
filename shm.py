import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import TextBox
from matplotlib.widgets import Button

fig = plt.figure()

class main():
    def __init__(self):
        self.amp = 1
        self.t_period = 1
        self.damp_cnst = 1
        self.mass = 1

    def update_amp(self, event):
        if float(self.amp_box.text) > 0:
            self.amp = float(self.amp_box.text)
        else:
            self.amp = 1

    def update_t_period(self, event):
        if float(self.tp_box.text) > 0:
            self.t_period = float(self.tp_box.text)
        else:
            self.t_period = 1

    def update_damp_cnst(self, event):
        if float(self.dp_box.text) > 0:
            self.damp_cnst = float(self.dp_box.text)
        else:
            self.damp_cnst = 1

    def update_mass(self, event):
        if float(self.mass_box.text) > 0:
            self.mass = float(self.mass_box.text)
        else:
            self.mass = 1

    def init(self):
        ball_centre = 0, 5
        ball = self.p1.plot(0, 5, 'ro')
        return ball

    def animate(self, i):
        amp = self.amp
        t = self.t_period
        b = self.damp_cnst
        m = self.mass

        w = 2 * np.pi / t
        w_ = abs((w ** 2 - (b ** 2 / (4 * m))) ** 0.5)

        x = amp * np.exp(-b * i/ (2 * m * 50)) * np.cos(w_ * i / 50)

        ball_centre = x, 5
        ball = self.p1.plot(x, 5, 'ro')
        return ball

    def go(self, event): 
        amp = self.amp
        t = self.t_period
        b = self.damp_cnst
        m = self.mass

        w = 2 * np.pi / t
        w_ = (w ** 2 - (b ** 2 / (4 * m))) ** 0.5

        fig.clf()


        back_box = plt.axes([0.8, 0.9, 0.07, 0.075])
        self.back_button = Button(back_box, "Back")
        self.back_button.on_clicked(self.back)
        self.p1 = fig.add_subplot(211)
        self.p2 = fig.add_subplot(212)

        self.p1.set_xlim(-amp - 2, amp + 2)
        self.p1.set_ylim(0, 10)
        self.p1.get_yaxis().set_visible(False)
        self.p1.plot([-amp, amp], [5]*2)

        self.p2.set_ylim(-amp, amp)
        self.p2.set_xlim(0, 10*t)
        self.p2.plot([0, 10*t], [0]*2, 'y')

        self.p2.set_xlabel('Time')
        self.p2.set_ylabel('Displacement')

        x = np.arange(0, 10 * t, 0.01)
        y = amp * np.exp(-b / (2 * m) * x) * np.cos(w_ * x)
        line, = self.p2.plot(x, y)

        self.anim = animation.FuncAnimation(fig, self.animate,
                                        init_func=self.init,
                                        interval=20,
                                        blit=True)

        plt.draw()


    def init_page(self):

        fig.text(0.2, 0.8, 'SIMPLE HARMONIC MOTION', fontsize = 50)

        amp_box_loc = plt.axes([0.4, 0.5, 0.2, 0.075])
        self.amp_box = TextBox(amp_box_loc, 'Amplitude (A)', initial=str(self.amp))
        tp_box_loc = plt.axes([0.4, 0.4, 0.2, 0.075])
        self.tp_box = TextBox(tp_box_loc, 'Time Period (T)', initial=str(self.t_period))
        dc_box_loc = plt.axes([0.4, 0.3, 0.2, 0.075])
        self.dp_box = TextBox(dc_box_loc, 'Damping Constant (b)', initial=str(self.damp_cnst))
        mass_box_loc = plt.axes([0.4, 0.2, 0.2, 0.075])
        self.mass_box = TextBox(mass_box_loc, 'Mass of ball (m)', initial=str(self.mass))

        bbox1 = plt.axes([0.45, 0.1, 0.1, 0.075])
        self.button1 = Button(bbox1, "GO!")

        self.amp_box.on_submit(self.update_amp)
        self.tp_box.on_submit(self.update_t_period)
        self.dp_box.on_submit(self.update_damp_cnst)
        self.mass_box.on_submit(self.update_mass)
        self.button1.on_clicked(self.go)
        plt.draw()

    def back(self, event):
        fig.clear()
        try:
            self.anim.event_source.stop()
        except:
            None
        return self.init_page()

main().init_page()
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()







