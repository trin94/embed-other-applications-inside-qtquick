import QtQuick
import QtQuick.Controls.Material
import pyobjects

ApplicationWindow {
    id: mainWindow

    width: 600
    height: 600
    visible: true

    Material.theme: Material.Dark

    Item {
        id: someItem
        anchors.margins: 100
        anchors.fill: parent

        WindowContainer {
            anchors.fill: parent
            id: windowContainer

            window: MpvItem {
                id: mpvItem
            }
        }

        Window {
            parent: someItem
            visible: true
            width: parent.width

            MenuBar {
                id: menuBar

                Menu {
                    title: 'MENU 1'

                    MenuItem { text: 'Action 11' }
                    MenuItem { text: 'Action 12' }
                    MenuItem { text: 'Action 13' }
                    MenuItem { text: 'Action 14' }
                    MenuItem { text: 'Action 15' }
                }

                Menu {
                    title: 'MENU 2'

                    MenuItem { text: 'Action 21' }
                    MenuItem { text: 'Action 22' }
                    MenuItem { text: 'Action 23' }
                    MenuItem { text: 'Action 24' }
                    MenuItem { text: 'Action 25' }
                }
            }
        }
    }

    MouseArea {
        id: mouseArea

        anchors.fill: parent
        acceptedButtons: Qt.LeftButton | Qt.RightButton
        cursorShape: Qt.OpenHandCursor

        onClicked: mpvItem.play()
    }
}