from logging import exception
from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,StreamingHttpResponse
from senas.cam import video_generator, videos, video_generator_solution


def index(request):
    return render(request, 'senas/video.html', {})

def video(request):
    return render(request, 'senas/video.html', {})


def stream(request):
    try:
        return StreamingHttpResponse(video_generator(videos()),content_type="multipart/x-mixed-replace;boundary=frame")
    except exception as e:
        print("aborted")

def stream_hand(request):
    try:
        return StreamingHttpResponse(video_generator_solution(videos()),content_type="multipart/x-mixed-replace;boundary=frame")
    except exception as e:
        print("aborted")