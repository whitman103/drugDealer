#include <qt5/QtWidgets/QApplication>
#include <qt5/QtWidgets/QPushButton>

int main(int argc, char** argv){
    QApplication app(argc, argv);

    QPushButton button ("Hello World!");
    button.show();

    return app.exec();


}
