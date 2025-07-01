from ultralytics import YOLO

def main():
    model = YOLO("yolov8s.pt")  # or yolov8s.pt or any custom model

    model.train(
        data="roboflow/data.yaml",
        epochs=100 ,
        imgsz=1280, 
        
        batch=8,
        name="yolov8-highres",
        project="shrink_detect"
    )

if __name__ == "__main__":
    from multiprocessing import freeze_support
    freeze_support()
    main()
