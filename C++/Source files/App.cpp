#include "App.h"

wxIMPLEMENT_APP(App);

App::App()
	: mainFrame(nullptr)
{

}

App::~App()
{

}

bool App::OnInit()
{
	mainFrame = new MainFrame();
	mainFrame->Show();

	return true;
}
