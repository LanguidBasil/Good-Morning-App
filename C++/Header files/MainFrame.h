#pragma once
#include "wx/wx.h"
#include "BarTop.h"

class MainFrame : public wxFrame
{
public:
	MainFrame();
	~MainFrame();

private:
	BarTop* barTop;
};
