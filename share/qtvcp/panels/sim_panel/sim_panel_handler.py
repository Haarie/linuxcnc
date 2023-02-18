############################
# **** IMPORT SECTION **** #
############################
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from qtvcp.core import Status, Action

# Set up logging
from qtvcp import logger

###########################################
# **** instantiate libraries section **** #
###########################################

STATUS = Status()
ACTION = Action()
LOG = logger.getLogger(__name__)
# Set the log level for this module
#LOG.setLevel(logger.INFO) # One of DEBUG, INFO, WARNING, ERROR, CRITICAL

###################################
# **** HANDLER CLASS SECTION **** #
###################################

class HandlerClass:

    ########################
    # **** INITIALIZE **** #
    ########################
    # widgets allows access to  widgets from the qtvcp files
    # at this point the widgets and hal pins are not instantiated
    def __init__(self, halcomp,widgets,paths):
        self.hal = halcomp
        self.w = widgets
        self.PATHS = paths
    ##########################################
    # Special Functions called from QTVCP
    ##########################################

    # at this point:
    # the widgets are instantiated.
    # the HAL pins are built but HAL is not set ready
    def initialized__(self):
        self.w.setFocusPolicy(Qt.NoFocus)
        print(self.w.parent())
        for widget in self.w.children():
            print(widget)
            try:
                widget.setFocusPolicy(QtCore.Qt.NoFocus)
            except:
                pass
        number = 0
        if self.w.USEROPTIONS_ is not None:
            LOG.debug('sim_panel user options: {}'.format(self.w.USEROPTIONS_))
            for num, i in enumerate(self.w.USEROPTIONS_):

                # override the default width and height of the window
                if 'size=' in self.w.USEROPTIONS_[num]:
                    try:
                        strg = self.w.USEROPTIONS_[num].strip('size=')
                        arg = strg.split(',')
                        self.w.resize(int(arg[0]),int(arg[1]))
                    except Exception as e:
                        print('Error with sim_panel size setting:',self.w.USEROPTIONS_[num])
                elif 'hide=' in self.w.USEROPTIONS_[num]:
                    try:
                        strg = self.w.USEROPTIONS_[num].strip('hide=')
                        arg = strg.split(',')
                        for i in arg:
                            print (i)
                            try:
                                self.w[i].hide()
                            except:
                                pass
                    except Exception as e:
                        print('Error with sim_panel size setting:',self.w.USEROPTIONS_[num])

    ########################
    # callbacks from STATUS #
    ########################

    #######################
    # callbacks from form #
    #######################

    #####################
    # general functions #
    #####################

    #####################
    # KEY BINDING CALLS #
    #####################

    ###########################
    # **** closing event **** #
    ###########################

    ##############################
    # required class boiler code #
    ##############################

    def __getitem__(self, item):
        return getattr(self, item)
    def __setitem__(self, item, value):
        return setattr(self, item, value)

################################
# required handler boiler code #
################################

def get_handlers(halcomp,widgets,paths):
     return [HandlerClass(halcomp,widgets,paths)]