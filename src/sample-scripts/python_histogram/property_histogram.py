import sys
import os

import pygtk
import gtk
import gtk.glade

class App:
	# �������������
	def __init__(self):
		# ��������� ���� � �����������
		self.gladefile = "property_hist.glade"
		
		# ������ ��������� ����������
		self.widgetsTree = gtk.glade.XML(self.gladefile)
		
		# ������� ������ < ������� - ���������� >
		dic =
			{
				# ������������ ������ ����� ���������� ��������
				"new_bins_number_selected" : self.new_bins_number_selected,
			}
	
		# ���������� �������� � ������������
		self.widgetsTree.signal.autoconnect(dic)
		
		# ���������� ������� �������� ���� � ������� ���������� ����������
		self.window = self.widgetsTree.get_widget("property_hist")
		if(self.window):
			self.window.connect("destroy", self.close_app)
		
		# ��������� �������� �� ���������
		self.bins = 50
		
		# ����� ������� �� �����
		#self.graphview = self.wTree.get_widget("histogram_box")
		#self.graphview.pack_start(self.canvas, True, True)
		
	def new_bins_number_selected(self, widget):
		# ����� ����� ������� �� ���������� ���� ����� � ������������ ������ �����������

		
	# �������� ����������
	def close_app(self, widget):
		gtk.main_quit()

if __name__ == "__main__":
	app = App()
	gtk.main()