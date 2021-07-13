{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.6.4 64-bit ('base': conda)",
   "metadata": {
    "interpreter": {
     "hash": "e04390b745d7540077d5afc7ea9b350ff3db0922faee759c3145cf85f5ee4c0c"
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "source": [
    "\n",
    "- 2021-07-13\n",
    "- 실전 문제 큰수의 법칙\n",
    "\n",
    "- idea : 단순 그리디 문제\n",
    "         리스트를 내림차순으로 정렬 후 제일 큰 원소를 K번 더하면 그 다음 원소를 더함\n",
    "         \n"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "46\n"
     ]
    }
   ],
   "source": [
    "N,M,K=map(int,input().split())\n",
    "_list=sorted(list(map(int,input().split())),reverse=True)\n",
    "cnt=0 #K번을 셀 친구 \n",
    "answer=0\n",
    "for i in range(M):\n",
    "    if(cnt==K):\n",
    "        answer+=_list[1]\n",
    "        cnt=0\n",
    "    else:\n",
    "        answer+=_list[0]\n",
    "        cnt+=1\n",
    "print(answer)\n",
    "\n"
   ]
  },
  {
   "source": [
    "\n",
    "\n",
    "first=data[n-1]\n",
    "second=data[n-2]\n",
    "result=0\n",
    "while True:\n",
    "    for i in range(k):\n",
    "        if m==0:\n",
    "            break\n",
    "        result+=first\n",
    "        m-=1\n",
    "    if m==0:\n",
    "        break\n",
    "    result +=second\n",
    "    m-=1\n",
    "print(result)\n"
   ],
   "cell_type": "code",
   "metadata": {},
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}