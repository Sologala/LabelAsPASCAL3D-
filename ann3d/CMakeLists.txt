
file(GLOB_RECURSE SRC ./src/*.cpp)


add_executable(ann3d ${SRC} ./main.cpp)

target_include_directories(ann3d PUBLIC ./include/)
target_link_libraries(ann3d imgui_app_base)



