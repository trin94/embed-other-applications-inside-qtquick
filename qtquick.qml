import QtQuick
import QtQuick.Controls.Material
import pyobjects

ApplicationWindow {
    id: root

    title: "Click to start video playback - It works :)"
    width: 600
    height: 600
    visible: true
    // flags: Qt.FramelessWindowHint

    onClosing: mpvItem.terminate()

    Rectangle {
        id: windowWrapper
        height: root.height
        width: root.width

        Window {
            x: root.x
            y: root.y
            width: windowWrapper.width
            height: windowWrapper.height
            visible: true
            color: 'transparent'
            flags: Qt.FramelessWindowHint

            MenuBar {
                id: menuBar
                width: root.width

                Menu {
                    title: 'Menu'

                    MenuItem { text: 'Action 1' }
                    MenuItem { text: 'Action 2' }
                    MenuItem { text: 'Action 3' }
                }
            }

            Menu {
                id: contextMenu
                MenuItem { text: 'Context Action 1' }
                MenuItem { text: 'Context Action 2' }
                MenuItem { text: 'Context Action 3' }
            }

            MouseArea {
                id: mouseArea

                z: -1
                anchors.fill: parent
                acceptedButtons: Qt.LeftButton | Qt.RightButton
                cursorShape: Qt.PointingHandCursor

                onClicked: mouse => {
                    if (mouse.button === Qt.LeftButton) {
                        mpvItem.play()
                    } else if (mouse.button === Qt.RightButton) {
                        contextMenu.popup()
                    }
                }
            }
        }

        WindowContainer {
            y: menuBar.height
            height: root.height - menuBar.height
            width: root.width

            window: MpvItem {
                id: mpvItem
                flags: Qt.FramelessWindowHint
                color: "black"
            }
        }
    }
}