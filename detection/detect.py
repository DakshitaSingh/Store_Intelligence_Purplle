from ultralytics import YOLO


model = YOLO(
    "yolov8n.pt"
)


def detect_people(
    frame
):

    results = model.track(
        frame,
        persist=True,
        classes=[0],
        verbose=False
    )

    detections = []

    if (
        results[0].boxes is None
        or
        results[0].boxes.id is None
    ):
        return detections

    boxes = (
        results[0]
        .boxes
        .xyxy
        .cpu()
        .numpy()
    )

    ids = (
        results[0]
        .boxes
        .id
        .cpu()
        .numpy()
    )

    confs = (
        results[0]
        .boxes
        .conf
        .cpu()
        .numpy()
    )

    for box, track_id, conf in zip(
        boxes,
        ids,
        confs
    ):

        detections.append(
            {
                "track_id":
                int(track_id),

                "bbox":
                box.tolist(),

                "confidence":
                float(conf)
            }
        )

    return detections