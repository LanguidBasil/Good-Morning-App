#include "BarTop.h"

wxBEGIN_EVENT_TABLE(BarTop, wxPanel)
	EVT_PAINT(BarTop::OnPaint)
wxEND_EVENT_TABLE()

BarTop::BarTop(wxFrame* parent)
	: wxPanel(parent, 100, wxPoint(0, 0), wxSize(100, 100))
{
	
}

BarTop::~BarTop()
{

}

void BarTop::OnPaint(wxPaintEvent& evt)
{
	wxPaintDC dc(this);
	dc.DrawRectangle(wxPoint(0, 0), wxSize(400, 100));
}
