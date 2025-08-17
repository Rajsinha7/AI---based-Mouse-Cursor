# AI---based-Mouse-Cursor
This project implements a computer vision–based virtual mouse system that enables users to control their computer cursor and perform standard mouse operations through hand gestures detected via a webcam.

Using MediaPipe for real-time hand tracking and OpenCV for video processing, the system maps finger positions to screen coordinates and translates gestures into mouse actions with PyAutoGUI. The integration of a smoothing algorithm ensures stable and fluid cursor movement, minimizing jitter caused by natural hand motion.

Key Features:
Real-time Hand Tracking: Leverages MediaPipe’s robust hand landmark detection to track finger positions with high accuracy.
Gesture-to-Action Mapping:
Cursor Control → Index finger guides the mouse pointer.
Left Click → Pinch gesture (thumb + index finger).
Right Click → Pinch gesture (thumb + middle finger).
Drag & Drop → Bringing index and middle fingers close together to initiate drag mode.
Scrolling → Vertical finger positioning to trigger smooth scroll up/down.
Smoothing Mechanism: Implements a weighted moving average function to reduce noise and jitter in cursor movement.
Cross-Platform Compatibility: Works on any system supported by OpenCV, MediaPipe, and PyAutoGUI.

Applications:
Touchless Interaction: Ideal for hygienic, hands-free computer interaction in public spaces.
Accessibility Tool: Supports individuals with physical disabilities by providing an alternative input method.
Human-Computer Interaction Research: Useful in prototyping gesture-based UI systems.
