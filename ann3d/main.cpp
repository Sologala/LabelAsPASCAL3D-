#include "imapp/canvas/canvas.h"
#include "imapp/primitives/mesh.h"
#include "imgui_internal.h"
#include <imapp/imapp.h>

int main(int argc, char *argv[])
{

    ImGuiApp::AppBase::Option opt;
    opt.font_size = 30;
    ImGuiApp::AppBase app("test-app", ImVec2(1600, 900), opt);
    ImGuiCanvas       canvas("viewport");

    Mesh::Sptr mesh = std::make_shared<Mesh>("../resource/sedan.stl");
    mesh->SetAlpha(0.85f);
    canvas.AddDrawable("mesh", mesh, true);

    app.AddBeforeStartDrawing([&]() {
        app.RegistLayoutBegin();
        app.RegistLayout("", "top", "down", ImGuiDir_Up, 0.8f);
        app.RegistLayout("top", "viewport", "imgview", ImGuiDir_Left, 0.5f);
        app.RegistLayout("down", "log", "opt", ImGuiDir_Left, 0.5f);
        return true;
    });

    app.AddDrawCallBack([&]() {
        ImGui::Begin("imgview");
        ImGui::Button("Button 1");
        ImGui::Button("Button 2");
        ImGui::Button("Button 3");
        ImGui::End();
        return true;
    });

    app.AddDrawCallBack([&]() {
        ImGui::Begin("log");
        ImGui::Button("Button 1");
        ImGui::Button("Button 2");
        ImGui::Button("Button 3");
        ImGui::End();
        return true;
    });

    app.AddDrawCallBack([&]() {
        ImGui::Begin("opt");
        ImGui::Button("Button 1");
        ImGui::Button("Button 2");
        ImGui::Button("Button 3");
        ImGui::End();
        return true;
    });

    app.AddDrawCallBack([&]() {
        canvas.Draw();
        return true;
    });

    app.Run();

    return 0;
}
