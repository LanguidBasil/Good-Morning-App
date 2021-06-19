#include "MainFrame.h"

MainFrame::MainFrame() 
	: wxFrame(nullptr, 0, "Good Morning", wxPoint(200, 200), wxSize(400, 500)), 
	barTop(new BarTop(this))
{

}

MainFrame::~MainFrame()
{

}
