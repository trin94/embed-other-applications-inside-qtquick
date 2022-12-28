import QtQuick
import QtQuick.Controls
import pyobjects


ApplicationWindow {
    id: root

    width: 1280
    height: 720
    visible: true

    Menu {
        id: menu

        MenuItem { text: 'Action 1' }
        MenuItem { text: 'Action 2' }
        MenuItem { text: 'Action 3' }
        MenuItem { text: 'Action 4' }
        MenuItem { text: 'Action 5' }
    }

    Rectangle {
        id: container

        color: 'orange'
        anchors.fill: parent

        Rectangle {
            id: mouseRectangle

            x: videoArea.otherMargin
            y: 50
            width: videoArea.width
            height: videoArea.customTopMargin - (y + 25)
            color: 'blue'

            MouseArea {
                id: mouseArea

                anchors.fill: mouseRectangle
                acceptedButtons: Qt.LeftButton | Qt.RightButton
                cursorShape: Qt.OpenHandCursor

                onClicked: menu.popup()
            }
        }

        Rectangle {
            id: videoArea

            property var embedder: MyEmbedder {} // imported from b_container.py
            property int customTopMargin: 125
            property int otherMargin: 75

            color: 'transparent'
            anchors.fill: parent
            anchors.topMargin: customTopMargin
            anchors.bottomMargin: otherMargin
            anchors.leftMargin: otherMargin
            anchors.rightMargin: otherMargin

            function updateGeometry() {
                const point = mapToItem(container, Qt.point(videoArea.x - otherMargin, videoArea.y - customTopMargin))
                embedder.set_geometry(point.x, point.y, width, height)
            }

            onXChanged: updateGeometry()
            onYChanged: updateGeometry()
            onWidthChanged: updateGeometry()
            onHeightChanged: updateGeometry()

            Component.onCompleted: { updateGeometry(); embedder.schedule_init() }
        }
    }

}
