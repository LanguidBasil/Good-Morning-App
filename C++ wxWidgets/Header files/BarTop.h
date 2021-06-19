#pragma once
#include "wx/wx.h"

class BarTop : public wxPanel
{
public:
	BarTop(wxFrame* parent);
	~BarTop();

	void OnPaint(wxPaintEvent& evt);

	wxDECLARE_EVENT_TABLE();
};
	